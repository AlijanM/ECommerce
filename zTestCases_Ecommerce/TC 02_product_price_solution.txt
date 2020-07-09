//********************************************************************************************
//*    Guru99 eCommerce Live Project    
//*    Author      : Krishna Rungta                    
//********************************************************************************************
/*      
Test Steps:
1. Goto http://live.demoguru99.com/
2. Click on ‘MOBILE’ menu
3. In the list of all mobile , read the cost of Sony Xperia mobile (which is $100)
4. Click on Sony Xperia mobile
5. Read the Sony Xperia mobile from detail page. Product value in list and details page should be equal ($100). 
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

public class TestCase2 {
	  private WebDriver driver;
	  private String baseUrl;	
	  
	@BeforeTest
	public void setUp() throws Exception {
	    driver = new FirefoxDriver();
	    baseUrl = "http://live.demoguru99.com/";
	    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	  }
	  
	  @Test
	  public void testTestCase2() throws Exception {
		
		// 1. Go to http://live.demoguru99.com
	    driver.get(baseUrl); 
	    
	    // 2. Click on Mobile menu
	    driver.findElement(By.linkText("MOBILE")).click();	
	  
	    // 3. In the list of all mobile , read the cost of Sony Xperia mobile (which is $100) 	    	      
	    String XPeriaPrice = driver.findElement(By.cssSelector("#product-price-1 > span.price")).getText();
	   
	    // 4. Click on Sony Xperia mobile 	   
	    driver.findElement(By.id("product-collection-image-1")).click();
	    
	    // 5. Read the XPeria mobile price from details page
	    String detailPrice = driver.findElement(By.cssSelector("span.price")).getText();
	    	    
	    //  Product price in list and details page should be equal ($100)
	    try {
	        assertEquals(XPeriaPrice, detailPrice); 
	      } catch (Exception e) {
	    	  e.printStackTrace();
	      }
	  }
	
	@AfterTest
	public void tearDown() throws Exception {
		driver.quit();
	  }
	
	}
