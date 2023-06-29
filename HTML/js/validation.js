function checkFname()
{
    var f = document.frm.fname.value;
    var regu_exp=/^[A-Za-z]+$/           // Regular Expression for validation in javascipt.
    if (f=="")                           //this expression allowed only alphabets A-Z a-z.
	{
		document.getElementById("fname").innerHTML="Please Enter First Name";
    }
    else if (!regu_exp.test(f))        
    {
    	document.getElementById("fname").innerHTML="Please Enter Only Alphabets";
    }
	else
    {
        document.getElementById("fname").innerHTML="";
    }	
} 	

function checkLname()
{
    var f = document.frm.lname.value;
    var regu_exp=/^[A-Za-z]+$/           // Regular Expression for validation in javascipt.
    if (f=="")                           //this expression allowed only alphabets A-Z a-z.
	{
		document.getElementById("lname").innerHTML="Please Enter Last Name";
    }
    else if (!regu_exp.test(f))        
    {
    	document.getElementById("lname").innerHTML="Please Enter Only Alphabets";
    }
	else
    {
        document.getElementById("lname").innerHTML="";
    }	
}

function checkEmail()
{
    var f = document.frm.email.value;
    var regu_exp=/^[A-Za-z0-9-_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$/  //Regular Expression for validation in js.
    if (f=="")                                              
	{
		document.getElementById("email").innerHTML="Please Enter Mail";
    }
    else if (!regu_exp.test(f))        
    {
    	document.getElementById("email").innerHTML="Please Enter Valid Mail";
    }
	else
    {
        document.getElementById("email").innerHTML="";
    }	
} 	 	

function checkMobile()
{
    var f = document.frm.mnum.value;
    var regu_exp=/^\d{10}$/  //Regular Expression for validation in js.
    if (f=="")                                              
	{
		document.getElementById("mnum").innerHTML="Please Enter your Mobile number";
    }
    else if (!regu_exp.test(f))        
    {
    	document.getElementById("mnum").innerHTML="Please Enter only numbers with 10 digits";
    }
	else
    {
        document.getElementById("mnum").innerHTML="";
    }	
}

function checkMobileNew()
{
    var f = document.frm.mnum.value;
    var char=/^[0-9]+$/
    var length=/^[0-9]{10}$/
    if (f=="")                                              
	{
		document.getElementById("mnum").innerHTML="Please Enter your Mobile number";
    }
    else if (!length.test(f) && char.test(f))
    {
    	document.getElementById("mnum").innerHTML="Please Enter 10 digits number";
    }
    else if (!char.test(f)) 
    	{
    		document.getElementById("mnum").innerHTML="Please Enter only numbers";
    	}
	else
    {
        document.getElementById("mnum").innerHTML="";
    }
}    	 

function checkPassword()
{
    var f = document.frm.password.value;
    var regu_exp = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/
    if (f=="")                                              
	{
		document.getElementById("password").innerHTML="Please Enter your Password";
    }
    else if (!regu_exp.test(f))
    {
    	document.getElementById("password").innerHTML="Min 1 Upper,Lower,Digit and special char in between 8-15 length";
    }
	else
    {
        document.getElementById("password").innerHTML="";
    }
}    	 	 	 	

function check_C_Password()
{
    var p= document.frm.password.value;
    var cp = document.frm.cpassword.value;

    if (cp=="")                                              
	{
		document.getElementById("cpassword").innerHTML="Please Enter your Confirm Password";
    }
    else if (p != cp)
    {
    	document.getElementById("cpassword").innerHTML="Password & Confirm Password does not matched";
    }
	else
    {
        document.getElementById("cpassword").innerHTML="";
    }
}    	 	 	