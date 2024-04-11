import SearchBar from '../Components/SearchBar';
import List from '../Components/List';
import Filter from '../Components/Filter'
function Home() {
  return (
    <div>
      <div>
        <SearchBar/>
      </div>
      <div style={{}}> 
        <div>
          <Filter/>
        </div>
        <div>
          <List/>
        </div>
      </div>
    </div>
  );
}

export default Home;
