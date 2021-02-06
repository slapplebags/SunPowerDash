#include <M5EPD.h>
#include <WiFi.h>

M5EPD_Canvas canvas(&M5.EPD);

void setup()
{
    M5.begin();
    M5.EPD.SetRotation(0);
    M5.EPD.Clear(true);
        canvas.createCanvas(960, 540);
    //WiFi.begin("TK-421", "thepasswordis...");
    WiFi.begin("OpenWrt", "");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

}

void loop()
{
    //canvas.createCanvas(540, 960);
    //canvas.setTextSize(3);
    //canvas.drawJpgUrl("https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/example_pic/flower.jpg");
    //canvas.pushCanvas(0,0,UPDATE_MODE_GC16);
    //delay(10000);
    //canvas.drawJpgUrl("https://upload.wikimedia.org/wikipedia/commons/e/e8/Brain_chrischan.jpg");
    //canvas.pushCanvas(0,0,UPDATE_MODE_GC16);
    delay(10000);
    canvas.drawJpgUrl("https://raw.githubusercontent.com/slapplebags/SunPowerDash/main/images/fignet.jpeg");
    canvas.pushCanvas(0,0,UPDATE_MODE_GC16); 
        delay(10000);
    canvas.drawJpgUrl("https://raw.githubusercontent.com/slapplebags/SunPowerDash/main/images/figuse.jpeg");
    canvas.pushCanvas(0,0,UPDATE_MODE_GC16);     
        delay(10000);
    canvas.drawJpgUrl("https://raw.githubusercontent.com/slapplebags/SunPowerDash/main/images/figprod.jpeg");
    canvas.pushCanvas(0,0,UPDATE_MODE_GC16);  
            delay(10000);
    canvas.drawJpgUrl("https://raw.githubusercontent.com/slapplebags/SunPowerDash/main/images/figperprod.jpeg");
    canvas.pushCanvas(0,0,UPDATE_MODE_GC16);
                delay(10000);
    canvas.drawJpgUrl("https://raw.githubusercontent.com/slapplebags/SunPowerDash/main/images/figperused.jpeg");
    canvas.pushCanvas(0,0,UPDATE_MODE_GC16);
                delay(10000);
    canvas.drawJpgUrl("https://raw.githubusercontent.com/slapplebags/SunPowerDash/main/images/figpernet.jpeg");
    canvas.pushCanvas(0,0,UPDATE_MODE_GC16);
}
