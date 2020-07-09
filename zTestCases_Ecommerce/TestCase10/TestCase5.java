//********************************************************************************************
//*    Guru99 eCommerce Live Project    
//*    Participant : Krishna Rungta                     
//*                                                                                                                                                          
//********************************************************************************************
/*     Verify can create an account in e-Commerce site and can share wishlist to other poeple using email.  
Test Steps:
1. Go to http://live.demoguru99.com/
2. Click on my account link
3. Click Create an Account link and fill New User information except Email ID
4. Click Register
5. Verify Registration is done. Expected account registration done.
6. Go to TV menu
7. Add product in your wish list - use product - LG LCD
8. Click SHARE WISHLIST 
9. In next page enter Email and a message and click SHARE WISHLIST
10.Check wishlist is shared. Expected wishlist shared successfully. 

*/

package eCommerceLive;

import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.By;
import static org.junit.Assert.*;
import static org.testng.AssertJUnit.assertEquals;
import org.openqa.selenium.WebDriver;

public class TestCase5 {
	  private WebDriver driver;
	  private String baseUrl;
	  public String firstName = "BERRY";    // Firstname and Lastname will be placed    
	  public String lastName = "BERRYTWO";  // in a TestData EXCEL file at some stage
	  
	@BeforeTest
	public void setUp() throws Exception {
	    driver = new FirefoxDriver();
	    baseUrl = "http://live.demoguru99.com/";
	    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	  }
	  
	  @Test
	  public void testTestCase5() throws Exception {
		
		// 1. Go to http://live.demoguru99.com
	    driver.get(baseUrl); 
	    
	    // 2. Click on my account link
	    driver.findElement(By.linkText("MY ACCOUNT")).click();
	    Thread.sleep(2000);
	    
	    // switching to new window
	    for (String handle : driver.getWindowHandles()) {
	    	driver.switchTo().window(handle);
	    	}
	    
	    // 3a. Click Create an Account link 
	    driver.findElement(By.linkText("CREATE AN ACCOUNT")).click();
	    Thread.sleep(2000);
	    
	    // switching to new window
	    for (String handle : driver.getWindowHandles()) {
	    	driver.switchTo().window(handle);
	    	}
	    // 3b. and fill New User information 
	    driver.findElement(By.id("firstname")).clear();	   
	    driver.findElement(By.id("firstname")).sendKeys(firstName); 
	    driver.findElement(By.id("lastname")).clear();	    
	    driver.findElement(By.id("lastname")).sendKeys(lastName);
	    driver.findElement(By.id("email_address")).clear();
	    driver.findElement(By.id("email_address")).sendKeys("Berry123@tpg.com.au");
	    driver.findElement(By.id("password")).clear();
	    driver.findElement(By.id("password")).sendKeys("mar8mar");
	    driver.findElement(By.id("confirmation")).clear();
	    driver.findElement(By.id("confirmation")).sendKeys("mar8mar");
	    
	    // 4. Click Register
	    driver.findElement(By.xpath("//button[@title='Register']")).click();
	    Thread.sleep(2000);
	    
	    // switching to new window
	    for (String handle : driver.getWindowHandles()) {
	    	driver.switchTo().window(handle);
	    	}
	    
	    // 5. Verify Registration is done. Expected account registration done.
	    String vWelcome = ("WELCOME, " + firstName + " " + lastName + "!");
	    String tWelcome = driver.findElement(By.xpath(".//*[@id='top']/body/div[1]/div/div[1]/div/p")).getText();
	    System.out.println("tWelcome = "+tWelcome);
	    	    
	    try {	    	
	    	assertEquals(tWelcome, vWelcome);
		    } catch (Exception e) {
		    	e.printStackTrace();	    	
		    }	
	    
	    // 6. Go to TV menu	    
	    driver.findElement(By.xpath(".//*[@id='nav']/ol/li[2]/a")).click();
	    Thread.sleep(2000);
	    
	    // switching to new window
	    for (String handle : driver.getWindowHandles()) {
	    	driver.switchTo().window(handle);
	    	}
	    
	    // 7. Add product in your wish list - use product - LG LCD	    
	    driver.findElement(By.xpath("//li/a[@class='link-wishlist']")).click();
	    
	    Thread.sleep(2000);
	    
	    // switching to new window
	    for (String handle : driver.getWindowHandles()) {
	    	driver.switchTo().window(handle);
	    	}
	    
	    // 8. Click SHARE WISHLIST 
	    driver.findElement(By.xpath("//button[@title='Share Wishlist']")).click();
	    
	    Thread.sleep(2000);
	    
	    // switching to new window
	    for (String handle : driver.getWindowHandles()) {
	    	driver.switchTo().window(handle);
	    	}
	    
	    // 9. In next page enter Email and a message and click SHARE WISHLIST
	    driver.findElement(By.id("email_address")).clear();
	    driver.findElement(By.id("email_address")).sendKeys("support@guru99.com");
	    driver.findElement(By.id("message")).clear();
	    driver.findElement(By.id("message")).sendKeys("Hey Mary!! this LCD TV looks ok, check it out !!.. cheers .. Berry");
	    
	    driver.findElement(By.xpath("//button[@title='Share Wishlist']")).click();
	    // the above click will still be in the same page as prior page, so no need take another handle to another window	    
	    
	    Thread.sleep(2000);
	    
	    // 10. Check wishlist is shared. Expected wishlist shared successfully. 
	    String vWishList = "Your Wishlist has been shared.";
	    String wishList = driver.findElement(By.xpath(".//*[@id='top']/body/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li/ul/li/span")).getText();
	    System.out.println("wishList = "+wishList);
	    try {	    	
	    	assertEquals(vWishList, wishList);
		    } catch (Exception e) {
		    	e.printStackTrace();	    	
		    }	
	    	    
	    Thread.sleep(2000);
	  }
	
	@AfterTest
	public void tearDown() throws Exception {
		Thread.sleep(1000);
		driver.quit();
	  }
	}
