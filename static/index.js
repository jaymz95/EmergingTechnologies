(function()
{
    var canvas = document.querySelector( "#myCanvas" );
	var context = canvas.getContext( "2d" );
	canvas.width = 280;
	canvas.height = 280;

	
	debug();

    function debug()
	{
		/* CLEAR BUTTON */
		var clearButton = $( "#clearButton" );
		
		clearButton.on( "click", function()
		{
			
				context.clearRect( 0, 0, 280, 280 );
				context.fillStyle="white";
				context.fillRect(0,0,canvas.width,canvas.height);
			
		});

		/* COLOR SELECTOR */

		$( "#colors" ).change(function()
		{
			var color = $( "#colors" ).val();
			context.color = color;
		});
		
		/* LINE WIDTH */
		
		$( "#lineWidth" ).change(function()
		{
			context.lineWidth = $( this ).val();
		});
    }
}());