/*
Isla Johnston, Olivia McNamara
with Dr D Evangelista and N Troiano
*/

#include "mbed.h"
#include "platform/mbed_thread.h"
#include "stdio.h"

// Blinking rate in milliseconds
#define BLINKING_RATE_MS 500

int away_score = 0;
int home_score = 0;
InterruptIn away_inc(p5);
InterruptIn home_inc(p6);
InterruptIn reset(p7); 
BusOut away(p17,p18,p19,p20);
BusOut home(p24,p23,p22,p21);

void reset_callback(void){
    away_score = 0; // when the reset button is pressed, the scores are set to zero
    home_score = 0; 
    }
    
void away_inc_callback(void){
    away_score++; // when the increment away score button is pressed, it increments away_score
    }
    
void home_inc_callback(void){
    home_score++; // when the increment home score button is pressed it increments home_score
    }

int main(void){
    // register the callbacks
    reset.rise(&reset_callback); // rising edge interrupts - need to add RC debounce
    away_inc.rise(&away_inc_callback);
    home_inc.rise(&home_inc_callback); 
    
    // main game loop
    while(1) {
        away=away_score;
        home=home_score; 
        thread_sleep_for(BLINKING_RATE_MS);
    } // while(1)
} // main()
