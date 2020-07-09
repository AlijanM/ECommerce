/********************************************************************************************
//*    Guru99 eCommerce Live Project    
//*    Participant : Krishna Rungta                      
//*                                                                                                                                                        *
//********************************************************************************************
/*  Verify you are able to change or reorder previously added product
 *  Test Data = QTY = 10
Test Steps:
1. Go to http://live.demoguru99.com/
2. Click on my account link
3. Login in application using previously created credential
4. Click on 'REORDER' link , change QTY & click Update
5. Verify Grand Total is changed
6. Complete Billing & Shipping Information
7. Verify order is generated and note the order number

Expected outcomes:
1) Grand Total is Changed
2) Order number is generated
*/

package eCommerceLive;

import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.*;

public class TestCase8 {
	  private WebDriver driver;
	  private String baseUrl;
	  public String firstName = "BERRY";    // These testdata stuff will be placed    
	  public String lastName = "BERRYTEN";  // in a TestData EXCEL file at some stage
	  public String vEmail = "Berry.Berrysix@gmail.com";
	  public String vPW = "123456";
	  public String vPrice, sPrice;
	  
	@BeforeTest
	public void setUp() throws Exception {
		System.setProperty("webdriver.chrome.driver", "c:\\chromedriver.exe");
	    driver = new ChromeDriver();
	    baseUrl = "http://live.demoguru99.com/";
	    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	  }
	  
	  @Test
	  public void testTestCase8() throws Exception {
		  
		  // Step 1. Go to http://live.demoguru99.com                                         
		    driver.get(baseUrl); 
		    
		    // Step 2. Click on My Account link
		    driver.findElement(By.linkText("MY ACCOUNT")).click();
		    
		    Thread.sleep(15000);  
		    
		    // switching to new window                                                    
		    for (String handle : driver.getWindowHandles()) {
		    	driver.switchTo().window(handle);
		    	}
		    
		    // Step 3. Login in application using previously created credential 
		    driver.findElement(By.id("email")).clear();	   
		    driver.findElement(By.id("email")).sendKeys(vEmail); 
		    driver.findElement(By.id("pass")).clear();	    
		    driver.findElement(By.id("pass")).sendKeys(vPW);
		    driver.findElement(By.id("send2")).click();	 // this is the Login button   
		    
		    Thread.sleep(5000);  
		    
		    // switching to new window                                                                               
			    for (String handle : driver.getWindowHandles()) {
			    	driver.switchTo().window(handle);
			    	}
		  
			    // 4.Click on 'REORDER' link , change QTY & click Update
			    System.out.println("*** Before Reorder ***");
			    driver.findElement(By.linkText("REORDER")).click();
			    System.out.println("*** After Reorder ***");
			    
			    
			    // *  Get the Grand Total Price 
			    vPrice = driver.findElement(By.xpath(".//*[@id='shopping-cart-totals-table']/tfoot/tr/td[2]/strong/span")).getText();
			    
			    // switching to new window                                                                               
			    /*for (String handle : driver.getWindowHandles()) {
			    	driver.switchTo().window(handle);
			    	}*/
			    
			    // this will change the QTY	
			    driver.findElement(By.xpath("//input[@title='Qty']")).clear();
			    driver.findElement(By.xpath("//input[@title='Qty']")).sendKeys("10");
			    System.out.println("*** QTY  Set ***");
			    
			    // this will click the Update button			    
			    //driver.findElement(By.cssSelector("td.product-cart-actions > button[name=update_cart_action]")).click();
			    System.out.println("*** Cart Updated ***");
			    
                // this will check the Grand Total price after being updated 			    
			    sPrice = driver.findElement(By.xpath(".//*[@id='shopping-cart-totals-table']/tfoot/tr/td[2]/strong/span")).getText();			    
			    System.out.println("sPrice ="+sPrice);
			    
			    // verify the before and after Grand Total price, to confirm it has changed
			    if (vPrice== sPrice){
			    	   System.out.println("*** Grand Total price has not changed. ***");
			    }else{
				       System.out.println("*** Grand Total price has changed. ***");
				}	
			    			    
			    // this could be the Proceed to Checkout button 
			    driver.findElement(By.xpath("//button[@type='button']")).click();
			    
			    
			    // switching to new window                                                                                  
			    for (String handle : driver.getWindowHandles()) {                                             
			    	driver.switchTo().window(handle);
			    	} 
			    
			    //
			    //*  BILLING ADDRESS
			    try {
			    	Select bAddr = new Select(driver.findElement(By.name("billing_address_id")));
			    	int bAddrSize = bAddr.getOptions().size();
			    	bAddr.selectByIndex(bAddrSize-1); 
				    } catch (Exception e) {
				    	//e.printStackTrace();
				    	System.out.println("No dropdown element present");
				    }
			  
			    driver.findElement(By.id("billing:firstname")).clear();
			    driver.findElement(By.id("billing:firstname")).clear();
			    driver.findElement(By.id("billing:firstname")).sendKeys(firstName); 
			    driver.findElement(By.id("billing:lastname")).clear();
			    driver.findElement(By.id("billing:lastname")).sendKeys(lastName); 
			    driver.findElement(By.id("billing:company")).clear(); 
			    
			    driver.findElement(By.id("billing:street1")).clear();
			    driver.findElement(By.id("billing:street1")).sendKeys("148 Crown Street"); 
			    new Select(driver.findElement(By.xpath("//select[@id='billing:country_id']"))).selectByIndex(14);
			    Thread.sleep(5000);	    
			    driver.findElement(By.id("billing:city")).clear();	
			    driver.findElement(By.id("billing:city")).sendKeys("Sydney"); 
			    driver.findElement(By.id("billing:region")).clear();
			    driver.findElement(By.id("billing:region")).sendKeys("New South Wales");
			    driver.findElement(By.id("billing:postcode")).clear();
			    driver.findElement(By.id("billing:postcode")).sendKeys("2000");
			    driver.findElement(By.id("billing:telephone")).clear();
			    driver.findElement(By.id("billing:telephone")).sendKeys("8850 6789"); 
			    
			    // check radio button to "Ship to different address" 
		        driver.findElement(By.id("billing:use_for_shipping_no")).click();
			    
		        // click the CONTINUE button 
			   
			    // after the click above, it is still on same web page: live.guru99.com/index.php/checkout/onepage/
			    driver.findElement(By.xpath(".//*[@id='billing-buttons-container']/button")).click();
			    
			    
			    // switching to new window                                                                                
			    for (String handle : driver.getWindowHandles()) {  
			    	driver.switchTo().window(handle);
			    	}  
			    Thread.sleep(2000); 
			    
			 
			    //*  SHIPPING ADDRESS
			    try {
			    	Select sAddr = new Select(driver.findElement(By.name("shipping_address_id")));
			    	int sAddrSize = sAddr.getOptions().size();
			    	sAddr.selectByIndex(sAddrSize-1); 
				    } catch (Exception e) {
				    	//e.printStackTrace();
				    	System.out.println("No dropdown element present");
				    }
			    
			  
			    Thread.sleep(2000);   
			   
			    driver.findElement(By.id("shipping:firstname")).clear();
			    driver.findElement(By.id("shipping:firstname")).clear();
			    driver.findElement(By.id("shipping:firstname")).sendKeys(firstName); 
			    driver.findElement(By.id("shipping:lastname")).clear();
			    driver.findElement(By.id("shipping:lastname")).sendKeys(lastName); 
			    driver.findElement(By.id("shipping:company")).clear(); 
			    
			    driver.findElement(By.id("shipping:street1")).clear();
			    driver.findElement(By.id("shipping:street1")).sendKeys("50 Berry Street"); 
			    driver.findElement(By.id("shipping:street2")).clear();
			    // shipping country must be selected first from dropdown
			    new Select(driver.findElement(By.xpath("//select[@id='shipping:country_id']"))).selectByIndex(14); 
			    // once Australia is selected, then the region and city becomes simply a text input, instead of dropdown
			    driver.findElement(By.id("shipping:region")).clear();
			    driver.findElement(By.id("shipping:region")).sendKeys("New Sounth Wales"); 
			    driver.findElement(By.id("shipping:city")).clear();
			    driver.findElement(By.id("shipping:city")).sendKeys("Sydney"); 
			    driver.findElement(By.id("shipping:postcode")).clear();
			    driver.findElement(By.id("shipping:postcode")).sendKeys("2000"); 
			    driver.findElement(By.id("shipping:telephone")).clear();
			    driver.findElement(By.id("shipping:telephone")).sendKeys("8034 1234");
			        
			    Thread.sleep(3000);	    
			    
			    driver.findElement(By.xpath(".//*[@id='shipping-buttons-container']/button")).click(); 
			    			    
			    // switching to new window                                                                                
			    for (String handle : driver.getWindowHandles()) {  
			    	driver.switchTo().window(handle);
			    	}  
			    Thread.sleep(3000); 
			    
			 // In Shipping Method, Click Continue 			    
			    driver.findElement(By.xpath(".//*[@id='shipping-method-buttons-container']/button")).click(); 
			   	 
			    Thread.sleep(2000);
			    
			    // In Payment Information select 'Check/Money Order' radio button. Click Continue			    
			    driver.findElement(By.xpath("//input[@title='Check / Money order']")).click();
			    
			    
			    Thread.sleep(2000);				   
			    driver.findElement(By.xpath(".//*[@id='payment-buttons-container']/button")).click(); 
			   
			    Thread.sleep(2000);
			    
			    // Click 'PLACE ORDER' button 
			    driver.findElement(By.xpath(".//*[@id='review-buttons-container']/button")).click();
			    
			    Thread.sleep(2000);
			    
			    // Verify Order is generated. Note the order number 
			    String orderNum = driver.findElement(By.xpath(".//*[@id='top']/body/div[1]/div/div[2]/div/div/p[1]/a")).getText();	
			    System.out.println("*** Your order number for your record = " + orderNum);
	  }
	
	@AfterTest
	public void tearDown() throws Exception {
		Thread.sleep(3000);
		driver.quit();
	  }
	}
