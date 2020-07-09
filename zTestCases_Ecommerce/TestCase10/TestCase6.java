//********************************************************************************************
//*    Guru99 eCommerce Live Project    
//*    Participant : Krishna Rungta                     
//*                                                                                                                                                        *
//********************************************************************************************
/*  Verify user is able to purchase product using registered email id(USE CHROME BROWSER)     
Test Steps:
1. Go to http://live.demoguru99.com/
2. Click on my account link
3. Login in application using previously created credential
4. Click on MY WISHLIST link 
5. In next page, Click ADD TO CART link
6. Enter general shipping country, state/province and zip for the shipping cost estimate
7. Click Estimate 
8. Verify Shipping cost generated 
9. Select Shipping Cost, Update Total 
10. Verify shipping cost is added to total 
11. Click "Proceed to Checkout"
12a. Enter Billing Information, and click Continue
12b. Enter Shipping Information, and click Continue
13. In Shipping Method, Click Continue
14. In Payment Information select 'Check/Money Order' radio button. Click Continue
15. Click 'PLACE ORDER' button 
16. Verify Oder is generated. Note the order number

NOTE: PROCEED TO CHECKOUT (step 6 ) was taken out, so as to allow the Estimate button step to get processed. 
      Rest of the steps renumbered accordingly. 
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

import static org.junit.Assert.*;

public class TestCase6 {
	  private WebDriver driver;
	  private String baseUrl;
	  public String firstName = "BERRY";    // These testdata stuff will be placed    
	  public String lastName = "BERRYSEVEN";  // in a TestData EXCEL file at some stage
	  public String vEmail = "Berry.Berrysix@tpg.com.au";
	  public String vPW = "123456";
	  
	@BeforeTest
	public void setUp() throws Exception {
		System.setProperty("webdriver.chrome.driver", "c:\\chromedriver.exe");
	    driver = new ChromeDriver();
	    baseUrl = "http://live.demoguru99.com/";
	    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	  }
	  
	  @Test
	  public void testTestCase6() throws Exception {
		
		// 1. Go to http://live.demoguru99.com                                         
	    driver.get(baseUrl); 
	    
	    
	    // 2. Click on my account link                                             
	    driver.findElement(By.linkText("MY ACCOUNT")).click();
	    
	    Thread.sleep(3000);  
	    
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
	   
	    Thread.sleep(3000);  
	    
	 // switching to new window                                                                               
	    for (String handle : driver.getWindowHandles()) {
	    	driver.switchTo().window(handle);
	    	}
	    
	    // 4. Click on MY WISHLIST link                                                                              
	    driver.findElement(By.linkText("MY WISHLIST")).click();
	
	    Thread.sleep(3000);    
	    
	    // switching to new window                                                                             
	    for (String handle : driver.getWindowHandles()) {
	    	driver.switchTo().window(handle);
	    	}
	    
	    // 5. In next page, Click ADD TO CART link                                                                     
	    driver.findElement(By.xpath("//button[@title='Add to Cart']")).click();
	 
	    Thread.sleep(3000);   
	    
	    // switching to new window                                                                                  
	    for (String handle : driver.getWindowHandles()) {                                             
	    	driver.switchTo().window(handle);
	    	} 
	    
	    // 6. Enter general shipping country, state/province and zip for the shipping cost estimate                
	    new Select(driver.findElement(By.xpath("//select[@id='country']"))).selectByIndex(14);
	    driver.findElement(By.id("region")).sendKeys("New South Wales");
	    driver.findElement(By.id("postcode")).sendKeys("2000");
	    
	    // 7. Click Estimate                                                                                                       
	    driver.findElement(By.xpath(".//*[@id='shipping-zip-form']/div/button")).click(); // this is the ESTIMATE link
	    
	    
	    // 8. Verify Shipping cost generated                                                                               
	    String sFlatRate = "Flat Rate";
	    String flatRate = driver.findElement(By.xpath(".//*[@id='co-shipping-method-form']/dl/dt")).getText();	
	    try {
	    	System.out.println("sFlatRate = "+sFlatRate);
	    	System.out.println("flatRate = "+flatRate);
	    	assertEquals(sFlatRate, flatRate);
		    } catch (Exception e) {
		    	e.printStackTrace();	    	
		    }	
	    	    
	    String sFlatRatePrice = "Fixed - $5.00";
	    String flatRatePrice = driver.findElement(By.xpath(".//*[@id='co-shipping-method-form']/dl/dd/ul/li/label")).getText();
	    try {	 
	    	System.out.println("sFlatRatePrice = "+sFlatRatePrice);
	    	System.out.println("flatRatePrice = "+flatRatePrice);
	    	assertEquals(sFlatRatePrice, flatRatePrice);
		    } catch (Exception e) {
		    	e.printStackTrace();	    	
		    }	
	    
	    
	    // 9. Select Shipping Cost (already selected as default), Update Total                                              
	    driver.findElement(By.id("s_method_flatrate_flatrate")).click();	 // RADIO button  -  Fixed - $5.00
	    driver.findElement(By.xpath("//button[@title='Update Total']")).click();
	    
	    
	    
	    // 10. Verify shipping cost is added to total                                                           
	    String vFlatRatePrice = "$5.00";
	    String shippingCostIncluded = driver.findElement(By.xpath(".//*[@id='shopping-cart-totals-table']/tbody/tr[2]/td[2]/span")).getText();
	    
	    try {
	    	System.out.println("vFlatRatePrice = "+vFlatRatePrice);
	    	System.out.println("shippingCostIncluded = "+shippingCostIncluded);
	    	assertEquals(vFlatRatePrice, shippingCostIncluded);
		    } catch (Exception e) {
		    	e.printStackTrace();	    	
		    }
	   
	    
	    // 11. Click PROCEED TO CHECKOUT                                                                       
	    driver.findElement(By.xpath("//button[@title='Proceed to Checkout']")).click();
	   
	    Thread.sleep(3000);    
	    
	    
	    // switching to new window                                                                                
	    for (String handle : driver.getWindowHandles()) { 
	    	driver.switchTo().window(handle);
	    	}  
	    Thread.sleep(2000); 
	    
	    //********************************************************************************************************
	    //*
	    //*  BILLING ADDRESS
	    //*
	    //********************************************************************************************************
	    // Check if Select element is present. If not present, it is the first time a customer has logged back in, to process what is in his/her wishlist
	    
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
	    
	    //********************************************************************************************************
	    //*
	    //*  SHIPPING ADDRESS
	    //*
	    //********************************************************************************************************
	    // Check if Select element is present or not.  If not present, it is first time user has logged back in to process his/her order
	    
	    try {
	    	Select sAddr = new Select(driver.findElement(By.name("shipping_address_id")));
	    	int sAddrSize = sAddr.getOptions().size();
	    	sAddr.selectByIndex(sAddrSize-1); 
		    } catch (Exception e) {
		    	//e.printStackTrace();
		    	System.out.println("No dropdown element present");
		    }
	    
	  
	    Thread.sleep(3000);   
	   
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
	    Thread.sleep(2000); 
	    
	    
	    // 13. In Shipping Method, Click Continue   
	    driver.findElement(By.xpath(".//*[@id='shipping-method-buttons-container']/button")).click(); 	
	   	 
	    Thread.sleep(2000);
	    
	    // 14. In Payment Information select 'Check/Money Order' radio button. Click Continue
	    driver.findElement(By.xpath("//input[@title='Check / Money order']")).click();
	    
	    Thread.sleep(3000);	    
	    
	    driver.findElement(By.xpath(".//*[@id='payment-buttons-container']/button")).click(); 
	     
	    Thread.sleep(3000);
	    
	    // 15. Click 'PLACE ORDER' button  
	    driver.findElement(By.xpath(".//*[@id='review-buttons-container']/button")).click(); 
	    
	    Thread.sleep(3000);
	    
	    // 16. Verify Oder is generated. Note the order number 
	    String orderNum = driver.findElement(By.xpath(".//*[@id='top']/body/div[1]/div/div[2]/div/div/p[1]/a")).getText();	
	    System.out.println("*** Your order number for your record = " + orderNum);
	   
	  }
	
	@AfterTest
	public void tearDown() throws Exception {
		Thread.sleep(3000);
		driver.quit();
	  }
	}
