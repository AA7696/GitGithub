from flask import Flask, render_template, request, redirect, url_for

from Flask import app


@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.json
    itemName = data.get("itemName")
    itemDescription = data.get("itemDescription")
    # Save to MongoDB here
    return {"status": "success"}
