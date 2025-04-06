# WiFiVision - Detecção de Movimento com Sinais Wi-Fi

Projeto experimental que utiliza sinais de Wi-Fi para detectar movimentações em um ambiente, explorando a técnica de **análise de Channel State Information (CSI)**.

## Objetivo

Desenvolver um sistema que captura sinais Wi-Fi de um roteador local e analisa as variações para detectar movimento ou mudanças no ambiente, sem o uso de câmeras ou sensores tradicionais.

## Componentes do Projeto

- **Placa Wi-Fi compatível com CSI** (ex: Intel 5300)
- **Notebook com Linux Ubuntu (18.04 recomendado)**
- Driver modificado para extrair dados CSI
- Scripts de processamento de sinal (Python)
- Visualização gráfica (opcional)

## Pré-requisitos

- Placa Wi-Fi: **Intel 5300 AGN** (necessário para usar os drivers CSI)
- Sistema operacional: Linux Ubuntu 18.04 (ou kernel compatível)
- Dependências:
  - `numpy`, `matplotlib`, `scipy`, `pandas`
  - `tcpdump` ou outro sniffer de pacotes
  - Python 3

## Instalação

1. **Instalar driver CSI da Intel 5300**
   - Baixar e compilar o driver modificado:
     ```bash
     git clone https://github.com/dhalperi/linux-80211n-csitool
     cd linux-80211n-csitool
     sudo make install
     ```

2. **Coleta de dados**
   - Usar ferramenta `log_to_file` do repositório para capturar os pacotes com CSI:
     ```bash
     sudo ./log_to_file somefile.dat
     ```

3. **Análise dos dados**
   - Usar script Python para plotar e analisar variações de amplitude/fase.

## Funcionamento

- O notebook envia ou escuta pacotes Wi-Fi de um roteador local.
- O driver modificado registra o **estado do canal (CSI)** em tempo real.
- Variações no CSI indicam alterações no ambiente (ex: movimento humano).
- Os dados são processados e representados graficamente.

## Possibilidades futuras

- Implementar alertas por presença ou movimento.
- Treinar modelos de ML para reconhecer tipos de movimento.
- Combinar com sensores (IoT) para aplicações mais robustas.

## Créditos

Inspirado em:
- [CSI Tool - Intel 5300](https://dhalperi.github.io/linux-80211n-csitool/)
- Pesquisas da MIT, Stanford e Universidade Tsinghua sobre WiFi Sensing.

## Licença

MIT License. Livre para uso educacional e experimental.
