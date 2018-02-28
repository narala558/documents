// show toast
Toast.makeText(context, text, Toast.LENGTH_SHORT).show();


// sleep main thread
Handler handler=new Handler();
Runnable r=new Runnable() {
        public void run() {
            //what ever you do here will be done after 3 seconds delay.
        }
    };
handler.postDelayed(r, 3000);


// get button by id
Button navigation = (Button) findViewById(R.id.navigation);
navigation.setOnClickListener(
                              new View.OnClickListener() {
                                  @Override
                                  public void onClick(View view) {
                                      btSendMessage("10100,20200,30200");
                                  }
                              }
                              );
