// class SearchBar extends Component {
//   render () {
//     return (
//       <div>
//         <input value={this.props.searchText} onChange={this.props.onSearchChange} type="test" placeholder="Search..."/>
//         <br/>
//         <input checked={this.props.inStockOnlyCheckbox}
//           onChange = {this.props.onInStockOnlyCheckChange} id="instock" type="checkbox"/>
//         <label htmlFor="instock">Only show products in stock</label>
//       </div>
//     )
//   }
// }

// class ProductTable extends Component {
//   render () {
//     const rows = []
//     let currentCategory = null

//     const filteredData = this.props.data.filter((record) => record.name.includes(this.props.searchText))

//     filteredData.forEach((record) => {
//       if (record.category !== currentCategory) {
//         currentCategory = record.category
//         rows.push(<CategoryRow currentCategory={currentCategory}/>)
//       }
//       if (record.stocked || !this.props.inStockOnlyCheckbox) {
//         rows.push(<ProductRow record={record}/>) // What is record here?  It looks like a property? It's one of these two-way variables.
//       }
//     })

//     // Code before the breakdown into CategoryRow and ProductRow
//     // for (let i = 0; i < filteredData.length; i++) {
//     //   let record = filteredData[i]
//     //   let color = {color: 'black'}
//     //   if (!record.stocked) {
//     //     color = {color: 'red'}
//     //   }
//     //   if (record['category'] !== currentCategory) {
//     //     currentCategory = record['category']
//     //     rows.push(<tr><th colSpan={2}>{record['category']}</th></tr>)
//     //   }
//     //   if (record.stocked | !this.props.inStockOnlyCheckbox) {
//     //     rows.push(<tr><td style={color}>{record['name']}</td><td>{record['price']}</td></tr>)
//     //   }
//     // }

//     return (
//       <table>
//         <tbody>
//           <tr key='header'><th>Name</th><th>Price</th></tr>
//           {rows}
//         </tbody>
//       </table>
//     )
//   }
// }

// class CategoryRow extends Component {
//   render () {
//     return (
//       <tr key={this.props.currentCategory}><th colSpan={2}>{this.props.currentCategory}</th></tr>
//     )
//   }
// }

// class ProductRow extends Component {
//   render () {
//     let color = {color: 'black'}
//     if (!this.props.record.stocked) {
//       color = {color: 'red'}
//     }
//     const key = this.props.record.category + this.props.record.name
//     return (
//       <tr key={key}><td style={color}>{this.props.record.name}</td><td>{this.props.record.price}</td></tr>
//     )
//   }
// }