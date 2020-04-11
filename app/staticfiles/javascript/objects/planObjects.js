class DayOfWeek extends React.Component {
    preventDefault(event) {
      event.preventDefault();
    }
    drop(event) {
      var recipeGuid = event.dataTransfer.getData("text");
      var dayGuid;
      if (event.target.classList.contains("dayPlaceholder")){
        dayGuid = event.target.parentElement.id;
        event.target.parentElement.classList.remove('day_drag_hover');
      } else {
        dayGuid = event.target.id;
        event.target.classList.remove('day_drag_hover');
      }
      addRecipeToDay(recipeGuid,dayGuid);
    }
    onDragOver_handler(event){
      event.preventDefault();
      if (event.target.classList.contains("dayDrop")){
        event.target.classList.add('day_drag_hover');
      } else {
        event.target.parentElement.classList.add('day_drag_hover');
      }

    }
    onDragLeave_handler(event){
      event.preventDefault();
      if (event.target.classList.contains("dayDrop")){
        event.target.classList.remove('day_drag_hover');
      } else {
        event.target.parentElement.classList.remove('day_drag_hover');
      }
    }
    render() {
        return (
          <div className="panel panel-default">
            <div className="panel-heading">{this.props.dayName}</div>
            <div id={this.props.dayId} onDrop={this.drop} onDragOver={this.onDragOver_handler} onDragLeave={this.onDragLeave_handler} className="dayDrop emptyDay panel-body" >
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
