% graficar_ber.m
% Grafica BER vs Eb/N0 de cada modulacion (una figura por archivo CSV).
% Usa solo el segundo barrido (filas 16 a 30); el primero es calentamiento.

clear; clc; close all;

mods        = {'BPSK', 'QPSK', '8PSK'};
bits_punto  = 100000;          % bits_por_punto del barrido
cota        = 3/bits_punto;    % cota superior cuando no se observan errores
fila_ini    = 16;
fila_fin    = 30;

for k = 1:numel(mods)
    modn  = mods{k};
    fname = ['metricas_sistema_' modn '.csv'];

    if ~isfile(fname)
        warning('No se encontro %s, se omite.', fname);
        continue;
    end

    T = readtable(fname);

    if height(T) < fila_fin
        warning('%s tiene %d filas (< %d). Se usan las filas %d a %d disponibles.', ...
            fname, height(T), fila_fin, fila_ini, height(T));
        idx = fila_ini:height(T);
    else
        idx = fila_ini:fila_fin;
    end

    ebn0 = T.ebn0_db(idx);
    ber  = T.measured_ber(idx);

    % Separar mediciones reales de puntos sin errores
    real_mask = ber > 0;
    cero_mask = ~real_mask;

    % Curva teorica
    x   = 0:0.1:14;
    lin = 10.^(x/10);
    switch modn
        case {'BPSK', 'QPSK'}
            teo = 0.5*erfc(sqrt(lin));
        case '8PSK'
            teo = (2/3)*0.5*erfc(sqrt(3*sin(pi/8)^2*lin));
    end

    figure('Name', ['BER ' modn], 'Color', 'w');
    semilogy(x, teo, 'k-', 'LineWidth', 1.5); hold on;
    semilogy(ebn0(real_mask), ber(real_mask), 'bo-', 'LineWidth', 1.5, 'MarkerFaceColor', 'b');
    if any(cero_mask)
        semilogy(ebn0(cero_mask), cota*ones(nnz(cero_mask),1), 'rv', ...
            'MarkerSize', 8, 'LineWidth', 1.2);
        leyenda = {'Teorica', 'Medida', sprintf('Sin errores (BER < %.0e)', cota)};
    else
        leyenda = {'Teorica', 'Medida'};
    end

    grid on;
    xlabel('E_b/N_0 [dB]');
    ylabel('BER');
    title(['BER vs E_b/N_0 - ' modn]);
    legend(leyenda, 'Location', 'southwest');
    xlim([0 14]);
    ylim([1e-6 1]);

    saveas(gcf, ['BER_' modn '.png']);
end