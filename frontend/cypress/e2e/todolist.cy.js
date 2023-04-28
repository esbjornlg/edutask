describe('R8UC1', () => {
  let email = "Namn@gmail.com";
  let firstName = "Namn";
  let lastName = "Namnsson";
  before(function () {
    cy.visit('localhost:3000');
    cy.contains("div", "Email Address")
      .find("input[type=text]")
      .type(email);
    cy.get("input[value=Login]").click();

    let h1Text = "";
    cy.get('h1').invoke('text').then((text) => {
      h1Text = text;
    });
    //Create new account if it doesn't exist
    if (h1Text == "Login") {
      cy.get("input[value='Have no account yet? Click here to sign up.']").click();
      cy.contains("div", "First Name")
        .find("input[type=text]")
        .type(firstName);

      cy.contains("div", "Last Name")
        .find("input[type=text]")
        .type(lastName);
      cy.get("input[value='Sign Up']").click();
    }

    let task;
    let taskName = "Pawn Stars";
    let youtubeURL = "DRVlUDQCmNk";
    //try to find existing task
    cy.$$("a:contains('img')").then($task => {
      task = $task;
    })

    if (!task) {
      cy.contains("div", "Title")
        .find("input[type=text]")
        .type(taskName);
      cy.contains("div", "Youtube URL")
        .find("input[type=text]")
        .type(youtubeURL);

    }
  })


  it('Find input, type text, and click submit', () => {
    // Replace 'Your sample text here' with the text you want to type
    const textToType = 'Sample text here';

    // Find the input element by its placeholder and type the text
    cy.get('input[placeholder="Add a new todo item"]').type(textToType);

    // Click the submit button if it's enabled
    cy.get('input[type="submit"]').then(($submitButton) => {
      if (!$submitButton.prop('disabled')) {
        $submitButton.click();
      }
    });
  })

})
// describe('R8UC2 check', () => {

//   it('Checking if button icon is set to active ', () => {
//     cy.visit('https://localhost:3000')
//     cy.get('.checker.unchecked').click()
//     cy.get('.editable')
//       .should('have.css', 'text-decoration', 'line-through solid rgb(0, 0, 0)');
//   })
// })

// describe('R8UC2 uncheck', () => {

//   it('Checking if button icon is set to active ', () => {
//     cy.visit('https://localhost:3000')
//     cy.get('.checker.checked').click()
//   })
// })