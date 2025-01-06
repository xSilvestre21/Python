def calcula_total_leds(altura,largura):
    led_por_largura = largura + 1
    led_total = led_por_largura * (altura + 1)
    if altura == 0 or largura == 0:
      return 0
    return led_total

print(calcula_total_leds(3, 2))