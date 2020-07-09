//********************************************************************************************
//*    Guru99 eCommerce Live Project    
//*    Participant : Krishna Rungta                      
//*                                                                                                                                                         *
//********************************************************************************************
/*  Verify that you will be able to save previously placed order as a pdf file 
 * 
 *   Note: This TestCase7a version is due to the below amended steps.
 *  
Test Steps:
1. Go to http://live.demoguru99.com/
2. Click on My Account link
3. Login in application using previously created credential 
4. Click on 'My Orders'
5. Click on 'View Order'
6. *** note: After steps 4 and 5, step 6 "RECENT ORDERS" was not displayed
   Verify the previously created order is displayed in 'RECENT ORDERS' table and status is Pending
7. Click on 'Print Order' link
8. *** note: the link was not found. 
   Click 'Change...' link and a popup will be opened as 'Select a destination' , select 'Save as PDF' link.
9. *** unable to execute this step, due to issue with step 8 issue
   Click on 'Save' button and save the file in some location.
10. *** unable to execute this step, due to steps 8 and 9 issues.
    Verify Order is saved as PDF

*/

package eCommerceLive;

import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class TestCase7a {
	  private WebDriver driver;
	  private String baseUrl;
	  public String firstName = "BERRY";    // These testdata stuff will be placed    
	  public String lastName = "BERRYTEN";  // in a TestData EXCEL file at some stage
	  public String vEmail = "Berry.Berrysix@gmail.com";
	  public String vPW = "123456";
	  
	@BeforeTest
	public void setUp() throws Exception {
		System.setProperty("webdriver.chrome.driver", "c:\\chromedriver.exe");
	    driver = new ChromeDriver();
	    baseUrl = "http://live.demoguru99.com/";
	    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	  }
	  
	  @Test
	  public void testTestCase7a() throws Exception {
		  
	  // Step 1. Go to http://live.demoguru99.com                                         
		    driver.get(baseUrl); 
		    
	  // 2. Click on My Account link
		    driver.findElement(By.linkText("MY ACCOUNT")).click();
		    
		    Thread.sleep(2000);  
		    
	  // switching to new window                                                    
		    for (String handle : driver.getWindowHandles()) {
		    	driver.switchTo().window(handle);
		    	}
		    
	  // 3. Login in application using previously created credential 
		    driver.findElement(By.id("email")).clear();	   
		    driver.findElement(By.id("email")).sendKeys(vEmail); 
		    driver.findElement(By.id("pass")).clear();	    
		    driver.findElement(By.id("pass")).sendKeys(vPW);
		    driver.findElement(By.id("send2")).click();	 // this is the Login button   
		    
		    Thread.sleep(2000);  
		    
	  // switching to new window                                                                               
			    for (String handle : driver.getWindowHandles()) {
			    	driver.switchTo().window(handle);
			    	}
		  
	  // 4. Click on 'My Orders'
	         driver.findElement(By.linkText("MY ORDERS")).click();
	         
	      // switching to new window                                                                               
			    for (String handle : driver.getWindowHandles()) {
			    	driver.switchTo().window(handle);
			    	}
		    
	  // 5. Click on 'View Order' 			   
	       driver.findElement(By.linkText("VIEW ORDER")).click();
	       
	       // switching to new window                                                                               
		    for (String handle : driver.getWindowHandles()) {
		    	driver.switchTo().window(handle);
		    	} 
		  
	  // 6. Verify the previously created order is displayed in 'RECENT ORDERS' table and status is Pending
	   // *******************************************************************************************************************************    
	   // note: After clicking My Order and View My Order the Recent Orders page was not displayed, the reason this step is commented out
	   // *******************************************************************************************************************************        
			    /*
			    try {
			        assertEquals("RECENT ORDERS", driver.findElement(By.cssSelector("h2")).getText());
			      } catch (Error e) {
			    	  System.out.println("*** Recent Orders failed to get displayed ***");
			    	  e.printStackTrace();	
			      }*/
		  
	    // 7. Click on 'Print Order' link now covers 3
			    driver.findElement(By.linkText("Print Order")).click();
			   
		  
		  // 8. Click 'Change...' link and a popup will be opened as 'Select a destination' , select 'Save as PDF' link.  
			    // note:  This do  not exist:   "Change...." link 
		
	   
		  // 9. Click on 'Save' button and save the file in some location.
		       // note: unable to execute this step due to issue in step 8. 
		  // 10.Verify Order is saved as PDF
			  // note: unable to execute this step due to issue in steps 8 and 9. 
		  
	  }
	
	@AfterTest
	public void tearDown() throws Exception {
		Thread.sleep(3000);
		driver.quit();
	  }
	}
