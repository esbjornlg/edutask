describe("R8UC1", () => {
  let email = "Namn@gmail.com";
  let firstName = "Namn";
  let lastName = "Namnsson";
  beforeEach(function () {
    cy.visit("localhost:3000");
    cy.contains("div", "Email Address").find("input[type=text]").type(email);
    cy.get("input[value=Login]").click();

    let h1Text = "";
    cy.get("h1")
      .invoke("text")
      .then((text) => {
        h1Text = text;
      });
    //Create new account if it doesn't exist
    if (h1Text == "Login") {
      cy.get(
        "input[value='Have no account yet? Click here to sign up.']"
      ).click();
      cy.contains("div", "First Name").find("input[type=text]").type(firstName);

      cy.contains("div", "Last Name").find("input[type=text]").type(lastName);
      cy.get("input[value='Sign Up']").click();
    }

    let taskName = "Pawn Stars";
    let youtubeURL = "DRVlUDQCmNk";
    cy.contains("div", "Title")
      .find("input[type=text]")
      .type(taskName);
    cy.contains("div", "YouTube URL")
      .find("input[type=text]")
      .type(youtubeURL);
    cy.get(".container").then($container => {
      if ($container["0"].children.length > 1) {
        cy.get('a:has(img)')
          .first()
          .click();
      } else {
        cy.get('input[type="submit"][value="Create new Task"]').click();
      }
    })
  })


  it('R8UC1_1: Add new todo item with valid text', () => {
    cy.viewport(1000, 1000);
    let number = Math.floor(Math.random() * 10000);
    let textToType = "Shop at pawnstar" + number;
    addTodoItem(textToType);
  });

  it('R8UC1_2: Add new todo item with invalid text', () => {
    cy.viewport(1000, 1000);
    cy.get('[value="Add"]').should('have.attr', 'disabled');
  });

  it('R8UC3_1: Add and then remove a todo item', () => {
    cy.viewport(1000, 1000);
    let number = Math.floor(Math.random() * 10000);
    let textToType = "RemoveThisItem" + number;
    addTodoItem(textToType);
    cy.contains('li', textToType)
      .find('span.remover')
      .click()
      .then(() => {
        cy.contains("span.editable", textToType).should("not.exist");
      });
  });

});

function addTodoItem(todoName) {
  cy.get('input[placeholder="Add a new todo item"]').type(todoName);

  cy.get('input[type="submit"][value="Add"]').click()
    .then(() => {
      cy.contains("span.editable", todoName).should("exist");
    });
}



// describe("R8UC2 check", () => {
//   it("Checking if button icon is set to active ", () => {
//     cy.get(".checker.unchecked").click();
//     cy.get(".editable").should(
//       "have.css",
//       "text-decoration",
//       "line-through solid rgb(0, 0, 0)"
//     );
//   });
// });

// describe('R8UC2 uncheck', () => {

//   it('Checking if button icon is set to active ', () => {
//     cy.visit('https://localhost:3000')
//     cy.get('.checker.checked').click()
//   })
// })
