#include <EEPROM.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);

struct Antena{
  float azim;
  float elev;
};

#define azimute PORTD
#define elevacao PORTC
//#define waiting_time 2 //ou 2
int waiting_time = 1;
char buf[100];

int az;
int el;

void anti(int passos, int deltaT){
   int cont = 0;
  while(cont < passos){
    azimute = B00110000;
    delay(deltaT);
  
    azimute = B01100000;
    delay(deltaT);
  
    azimute = B11000000;
    delay(deltaT);
  
    azimute = B10010000;
    delay(deltaT);
    cont++;
    //Serial.println(cont);
  }
}

void horario(int passos, int deltaT){
  int cont = 0;
  while(cont < passos){
    azimute = B10010000;
    delay(deltaT);
  
    azimute = B11000000;
    delay(deltaT);
  
    azimute = B01100000;
    delay(deltaT);
  
    azimute = B00110000;
    delay(deltaT);
    cont++;
    //Serial.println(cont);
  }
}

void elevAH(int passos, int deltaT){
  int cont = 0;
  while(cont < passos){
    elevacao = B000011;
    delay(deltaT);
  
    elevacao = B000110;
    delay(deltaT);
  
    elevacao = B001100;
    delay(deltaT);
  
    elevacao = B001001;
    delay(deltaT);
    cont++;
    //Serial.println(cont);
  }
}

void elevH(int passos, int deltaT){
  int cont = 0;
  while(cont < passos){
    elevacao = B001001;
    delay(deltaT);
  
    elevacao = B001100;
    delay(deltaT);
  
    elevacao = B000110;
    delay(deltaT);
  
    elevacao = B000011;
    delay(deltaT);
    cont++;
    //Serial.println(cont);
  }
}

void vel(int dT){
  EEPROM.write(dT,0);  
}

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  /*
  for(int z = 8; z < 12; z++){
    pinMode(z, OUTPUT);
  }
  */
  DDRD = B11110000;
  DDRD = DDRD | B11110000;
  DDRC = B001111;
}

void loop() {
  Antena antena;
  if(Serial.available()> 0){
    //long ang = Serial.parseInt(SKIP_WHITESPACE);
    float ang = Serial.parseFloat(SKIP_WHITESPACE);
    if(ang > 0 && ang < 360){
      az = float(ang);
      //lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("       ");
      lcd.setCursor(0,0);
      String ms = "az: "+String(az);
      lcd.print(ms);
      //az = map(az,1.00,360.00,0,3060);
      az = map(az,1.00,360.00,0,2620);
      //int gammaAZ = EEPROM.read(0)*12;
      EEPROM.get(24,antena);
      float gammaAZ = antena.azim *100;
      float alfa = az-gammaAZ;
      alfa = (int)alfa;
      antena.azim = float(az/100.00);
      EEPROM.put(24,antena);
      if(alfa > 1){
        horario(alfa,4);
        azimute = B00000000;
      }
      else if(alfa < -1){
        anti(-alfa,4);
        azimute = B00000000;
      }
      /*
      else{
        lcd.clear();
      }
      */
    }
    else if(ang < 0 && ang > -91){
      el = float(-ang);
      //lcd.clear();
      lcd.setCursor(0,1);
      lcd.print("       ");
      lcd.setCursor(0,1);
      String m = "el: "+String(el);
      lcd.print(m);
      el = map(el,1.00,90.00,0,765);
      //int gammaEL = EEPROM.read(12)*12;
      EEPROM.get(24,antena);
      float gammaEL = antena.elev *100;
      float beta = el-gammaEL;
      beta = (int)beta;
      antena.elev = float(el/100.00);
      EEPROM.put(24,antena);
      if(beta > 0){
        elevH(beta,4);
        elevacao = B000000;
      }
      else if(beta < 0){
        elevAH(-beta,4);
        elevacao = B000000;
      }
      /*
      else{
        lcd.clear();
      }
      */
    }
    //Serial.println(az,el);
    //Serial.println(EEPROM.read(0));
    //Serial.println(EEPROM.read(12));
    Antena atual;
    EEPROM.get(24,atual);
    Serial.println(atual.azim);
    Serial.println(atual.elev);
    
  }
  
}
