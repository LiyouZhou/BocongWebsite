var flashyshow=new flashyslideshow({ //create instance of slideshow
	wrapperid: "myslideshow", //unique ID for this slideshow
	wrapperclass: "flashclass", //desired CSS class for this slideshow
	imagearray: [
	
	
		["banner/01.jpg", "", "", ""],
		["banner/02.jpg", "", "", ""],
		["banner/03.jpg", "", "", ""],
		["banner/04.jpg", "", "", ""]
		
		
	],
	pause: 4000, //pause between content change (millisec)
	transduration: 3000 //duration of transition (affects only IE users)
})
