from selenium.webdriver.common.by import By


class HomePageLocators:
    dummyUrl1 = "https://app-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80"
    dummyUrl2 = "https://app-staging.qlub.cloud/qr/ae/dummy-checkout/89/_/_/e4b9eac596"
    dummyUrl3 = "https://app-staging.qlub.cloud/qr/ae/dummy-checkout/88/_/_/a604e595eb"
    dummyUrl4 = "https://app-staging.qlub.cloud/qr/ae/dummy-checkout/87/_/_/122ac1556c"
    dummyUrl5 = "https://app-staging.qlub.cloud/qr/ae/dummy-checkout/86/_/_/808b16b149"

    PayNowButton = (By.XPATH,"//span[normalize-space()='Pay now']")
    SplitBillButton = (By.XPATH,"//span[text()=\"Split bill\"]")
    SelectCustomButton = (By.ID,"select-custom")
    DivideEquallyButton = (By.ID,"select-byShare")
    SelectByItemButton = (By.ID,"select-byItem")
    CustomInputTextArea = (By.ID,"fullWidth")
    ConfirmButton = (By.ID,"split-bill")
