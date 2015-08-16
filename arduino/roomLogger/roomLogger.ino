#include <PlotlyYun.h>
#include <YunMessenger.h>
#include <Bridge.h>
#include <Console.h>
#include "DHT.h"

// DHT STUFF
#define DHTPIN 5     
#define DHTTYPE DHT22   
DHT dht(DHTPIN, DHTTYPE);

plotly plotter1("9gl2ecsppx");
plotly plotter2("7lgckcopse");

void setup() {

    // start-up the bridge
    Bridge.begin();
    
    Serial.begin(9600);
    Serial.println("Started!");
    
    dht.begin();

    // RUN PYTHON script on YUN
    Process p;
    p.runShellCommand("/root/run_plotly.sh");
    while (p.running()){ ; } // do nothing until process finishes

    delay(2000);
    Console.begin();
    while (!Console) {
      ; // wait for Console port to connect.
    }

    Console.buffer(64);
    delay(2000);

    plotter1.timezone = "America/Montreal";
    plotter2.timezone = "America/Montreal";
}

void loop() {
    // DHT 
     float h = dht.readHumidity();
     float t = dht.readTemperature();
     
    // Graph data! Place the "y" value that you want to plot
    // the "x" value will automatically be a time-stamped value
    // Each "plotter" will send data to the same plot as separate lines
    plotter1.plot( h );
    plotter2.plot( t );

    // You can also set the "x" value manually
    // by placing a pair of points in the plot function:
//    plotter1.plot( millis(), analogRead(A0) );
//    plotter2.plot( millis(), analogRead(A1) );
    delay(100);
}
