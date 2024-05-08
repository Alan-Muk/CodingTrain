class Mover{
	constructor(x,y){
		this.pos = createVector(x,y)
		this.vel = createVector(0,0)
		this.acc = createVector(0,0)
		//this.vel.mult(random(3))
		
		
	}

	applyForce(force) {
		this.acc.add(force)
	}


	edges(){
		if (this.pos.y >= height){
			this.pos.y = height;
			this.vel.y *= -1;
		} `else if(this.pos.y <= height){
					this.pos.y = height/2
					this.vel.y *= -1
				}`
		if (this.pos.x >= width){
			this.pos.x = width
			this.vel.x *= -1
		} else if (this.pos.x <= 0){
			this.pos.x = 0;
			this.vel.x *= -1
		}
	}


	update(){

		//let mouse = createVector(mouseX,mouseY)
		//this.acc = p5.Vector.sub(mouse, this.pos)
		//this.acc.setMag(1)
		//this.acc.setMag(0.01)
		//this.acc = p5.Vector.random2D()
		this.vel.add(this.acc)
		//this.vel.limit(3)
		this.pos.add(this.vel)
		this.acc.set(0,0)
	}

	show(){
		stroke(255)
		strokeWeight(2)
		fill(255,100)
		ellipse(this.pos.x, this.pos.y, 32)
	}
}