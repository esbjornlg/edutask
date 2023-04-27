describe('R8UC1', () => {
  let email = "www@gmail.com";
  before(function () {
    cy.visit('localhost:3000');
    cy.contains("div", "Email Address")
    .find("input[type=text]")
    .type(email);
    cy.get("input[value=Login]").click();
  })


  it('Checking if ', () => {
    cy.get("h1").should("contain.text", "Your tasks, www www")
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