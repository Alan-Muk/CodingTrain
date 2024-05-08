/* autogenerated by Processing revision 1293 on 2024-04-18 */
import processing.core.*;
import processing.data.*;
import processing.event.*;
import processing.opengl.*;

import java.util.HashMap;
import java.util.ArrayList;
import java.io.File;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;

public class Hilbert extends PApplet {

int order = 8;
int N = PApplet.parseInt(pow(2, order));
int total = N * N;

PVector[] path = new PVector[total];

public void setup() {
  /* size commented out by preprocessor */;
  background(0);
  
  for (int i = 0; i < total; i++) {
    path[i] = hilbert(i);
    float len = width/N;
    path[i].mult(len);
    path[i].add(len/2, len/2);
  }

}

int counter = 0;
public void draw () {
  background(0);
  
  stroke(255);
  strokeWeight(2);
  noFill();
  beginShape();
  for (int i = 1; i < counter; i++) {
    line(path[i].x, path[i].y,path[i-1].x, path[i-1].y);
  }
  
  //strokeWeight(4);
  //for (int i = 0; i < path.length; i++) {
  //  point(path[i].x, path[i].y);
  //  //text(i, path[i].x+5, path[i].y);
  //}
  
  endShape();
  counter += 10;
  
  if (counter >= path.length) {
    counter = 0;
  }

}

public PVector hilbert(int i) {
  PVector[] points = {
    new PVector(0, 0),
    new PVector(0, 1),
    new PVector(1, 1),
    new PVector(1, 0),
   };
  
  
  
    int index = i & 3;
    PVector v = points[index];
    
    for (int j = 1; j < order; j++) {
      i = i >>> 2;
      index = i & 3;
      
      float len = pow(2,j);
      if (index == 0) {
        float temp = v.x;
        v.x = v.y;
        v.y = temp;
      } else if (index == 1) {
        v.y += len;
      } else if (index == 2) {
        v.x += len;
        v.y += len;
      } else if (index == 3) {
        float temp = len -1 -v.x;
        v.x = len -1 -v.y;
        v.y = temp;
        v.x += len;
      }
      
    }
    
    return v;
  
 
}


  

  
  

  


  public void settings() { size(1024, 1024); }

  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Hilbert" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
