#include <DFRobot_DHT11.h>
#include<Wire.h>
#include<LiquidCrystal_I2C.h>

#define DHT11_PIN 8

DFRobot_DHT11 DHT;
LiquidCrystal_I2C lcd(0x27, 20, 4);

void setup()
{
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.print("Temperature and");
  lcd.setCursor(0,1);
  lcd.print("Humidity Monitoring");
  delay(2000);
  lcd.clear();
  
}

void loop()
{  
  DHT.read(DHT11_PIN);
  Serial.println(DHT.humidity);
  lcd.setCursor(0,0);
  lcd.print("Humidity:");
  lcd.setCursor(10,0);
  lcd.print(DHT.humidity);
  lcd.setCursor(12,0);
  lcd.print("%");
  lcd.setCursor(0,1);
  lcd.print("Temperature:");
  lcd.setCursor(13,1);
  lcd.print(DHT.temperature);
  lcd.setCursor(15,1);
  lcd.print("C");
  delay(5000);  
}
