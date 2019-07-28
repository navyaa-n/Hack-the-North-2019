//My Name But Cooler
//Navya Narukulla 
//--------------------------------------------------------------------\\
//first a
int num=20, steps = 20;
float theta, angle;
Stripe[] stripes = new Stripe[steps];
//n line 1
int posX = 50;
int posY = 200;
int speedX = 5;
int speedY = 5;
int sz = 15;
//n line 2
int posX2 = 250;
int posY2 = 200;
int speedX2 = 5;
int speedY2 = 5;
int sz2 = 15;
//jumping heart
int c = 210;
boolean up = true;
boolean down = false;
int speed = 3;
//second a
int a = 0;
int mw;
int  mh; 
int r = 100;
float nC = 36;

void setup() {
  size(1500, 600);

  rectMode(CENTER);
  createStuff();
  //second a
  noStroke();
  mw = 1300;
  mh = 340;
}
void draw() {

  background(255);
  /////////////////////////////////////////////////////
  for (int i = 0; i < width; i++) {
    for (int j = 0; j < height; j++) {
      int r = (int) map(mouseX - i, 0, width, 0, 255);
      int g = (int) map(mouseY - j, 0, height, 0, 255);
      int b = (int) map(mouseX- width/2, -width, width, 0, 255);
      set(i, j, color(r, g, b));
    }
  }
  /////////////////////////////////////////////////////
  //heart
  // fill((250),random(0,255),random(0,255));
  fill(#ED161D);
  strokeWeight(10.0);
  strokeJoin(ROUND);
  beginShape();
  vertex(750, 450);
  vertex(646, 330);
  vertex(854, 330);
  endShape();
  ellipse(699, 300, 120, 120);
  ellipse(801, 300, 120, 120); 
  /////////////////////////////////////////////////////
  //second a
  fill(0, 50);

  for (int i = 1; i <= nC; i++)
  {
    fill(255, 200+sin(radians(a+(360/nC)*i))*55, 200+cos(a+(360/nC)*i)*55);
    ellipse(mw+sin(radians(a+(360/nC)*i))*r, mh+cos(radians(a+(360/nC)*i))*r, 10*(r/100), 10*(r/100));
  }
  a++;
  /////////////////////////////////////////////////////
  //small jumping heart
  strokeWeight(1); 

  fill(#ED161D);
  ellipse(740, c, 20, 20);
  ellipse (760, c, 20, 20);
  triangle(750, c+25, 730, c+3, 770, c+3);

  if ( c==30 ) { 
    down = true; 
    up = false;
  } else if ( c == 210 ) { 
    up = true; 
    down = false;
  }
  if ( up == true ) { 
    c = c - speed;
  } else if ( down == true ) { 
    c = c + speed;
  }
  /////////////////////////////////////////////////////
  //letter n
  strokeWeight(10);
  stroke(#02D3CE);  
  line(57, 140, 245, 460); //57, 140
  rect (250, 300, 10, 325);
  rect(50, 300, 10, 325);
  posX = posX + speedX;
  posY = posY + speedY;

  //borders x-axis

  if (posX - sz/2 <= 0) {
    speedX = -speedX;
  }

  if (posX + sz/2 >= 0) {
    speedX = -speedX;
  }

  //borders y-axis

  if (posY + sz/2 >= 450) {
    speedY = -speedY;
  }

  if (posY - sz/2 <= 130) {
    speedY = -speedY;
  }

  //bouncing ball
  stroke(0);
  strokeWeight(4);
  fill((250), random(0, 255), random(0, 255));

  ellipse(posX, posY, sz, sz);
  //letter n line 2
  posX2 = posX2 + speedX2;
  posY2 = posY2 + speedY2;

  //borders x-axis

  if (posX2 - sz2/2 <= 0) {
    speedX2 = -speedX2;
  }

  if (posX2 + sz2/2 >= 0) {
    speedX2 = -speedX2;
  }

  //borders y-axis

  if (posY2 + sz2/2 >= 450) {
    speedY2 = -speedY2;
  }

  if (posY2 - sz2/2 <= 130) {
    speedY2 = -speedY2;
  }

  //bouncing ball
  stroke(0);
  strokeWeight(4);
  fill((250), random(0, 255), random(0, 255));

  ellipse(posX2, posY2, sz2, sz2);
  ////////////////////////////////////////////////////////////////
  //letter y
  {
    strokeWeight(10);
    stroke(#FA629A);
    noFill();
    arc (1027, 290, 150, 170, radians(0), radians(180));
    line (1103, 290, 1103, 470);
    line (1009, 474, 1137, 435);
    arc (1048, 470, 110, 130, radians(0), radians(150));
    arc(1034, 500, 70, 70, PI, PI+QUARTER_PI);
  }
  {
    strokeWeight(10);
    stroke((250), random(0, 255), random(0, 255));
    noFill();
    arc (1020, 290, 150, 170, radians(0), radians(180));
    line (1096, 290, 1096, 470);
    line (1002, 474, 1130, 435);
    arc (1041, 470, 110, 130, radians(0), radians(150));
    arc(1027, 500, 70, 70, PI, PI+QUARTER_PI);
  }
  ////////////////////////////////////////////////////////////////
  //line for second a
  {
    strokeWeight(7);
    stroke(255);
    noFill();
    arc (1508, 345, 200, 300, radians(140), radians(220));
  }

  ////////////////////////////////////////////////////////////////
  //letter a
  noStroke();
  fill(0);
  rect (532, 355, 10, 200);

  translate(425, 358);
  fill(20, 20);
  noStroke();
  angle=0;
  for (int i=0; i<stripes.length; i++) {
    pushMatrix();
    rotate(angle);
    stripes[i].display();
    angle += (TWO_PI/steps);
    popMatrix();
  }
  theta += .0523;
}

void createStuff() {
  for (int i=0; i<steps; i++) {
    //int num = (int) random(5, 20);
    int c = (int) 255.0/steps*i;
    //float offSet = random(TWO_PI);
    //float offSet = noise(i/2.0)*TWO_PI;    
    float offSet = TWO_PI/steps*i;
    stripes[i] = new Stripe(c, offSet);
  }
}

class Stripe {
  int c;
  float offSet;

  Stripe(int _c, float _offSet) {
    c = _c;
    offSet = _offSet;
  }

  void display() {
    colorMode(HSB, 255, 100, 100);
    fill(c, 80, 80);
    int n = (int) map(sin(theta+offSet), -1, 1, 2, num);
    if (n>10) n = 10;
    for (int i=0; i<n; i++) {
      rect(30+i*8, 0, 4, 6+i*2);
    }
    colorMode(RGB);
  }
}

void mousePressed() {
  println(mouseX, mouseY);
}