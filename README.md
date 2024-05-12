# Selenium brauzerinə cookie faylın import edilməsi

Cookie məlumatlarını chrome brauzerindən export etmək üçün <a href="https://chromewebstore.google.com/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg" target="_blank">EditThisCookie</a> adlı 'extension'u yükləməliyik. 

Sonra cookie məlumatlarını import etm'k istədiyimiz web saytı açırıq və EditThisCookie vasitəsilə həmin web saytın cookie məlumatlarını kopyalayırıq.

Sonra kopyaladığımız məlumatları .js formatında olan fayla daxil edərək yaddaşa veririk.

Sonra selenium_browser_with_cookies.py faylında həmin .js formatında olan faylı seçirik və proqramı işə salırıq.

Vizual olaraq fərqi görkəm üçün ilk olaraq cookie məlumatları import edilmədən https://instagram.com/ web saytı açılacaq sonra import edilərək. 
