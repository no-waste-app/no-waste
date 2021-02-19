describe("Main page", function () {
  it("load", function () {
    cy.visit("/")

    cy.get('h1').should("contain", "No Waste")
  })
})