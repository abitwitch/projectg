class DayOfWeek extends React.Component {
    preventDefault(event) {
      event.preventDefault();
    }
    drop(event) {
      var recipeGuid = event.dataTransfer.getData("text");
      var dayGuid;
      if (event.target.classList.contains("dayPlaceholder")){
        dayGuid = event.target.parentElement.id;
      } else {
        dayGuid = event.target.id;
      }
      addRecipeToDay(recipeGuid,dayGuid);



    }
    render() {
        return (
          <div className="panel panel-default">
            <div className="panel-heading">{this.props.dayName}</div>
            <div id={this.props.dayId} onDrop={this.drop} onDragOver={this.preventDefault} className="dayDrop emptyDay panel-body">
              <div className="dayPlaceholder">drag and drop a recipe</div>
            </div>
          </div>

        );
    }
}

class Week extends React.Component {
    render() {
        var days = this.props.days;
        return (
          <div>
            {Object.keys(days).map((id, vals) => (
              <DayOfWeek key={id} dayId={days[id]['id']} dayName={days[id]["dayName"]}/>
            ))}
          </div>
        );
    }
}
