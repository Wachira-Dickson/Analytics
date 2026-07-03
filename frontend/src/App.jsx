import {Route, Routes} from 'react-router-dom'
import './App.css'
import HomePage from './components/HomePage'
import CreatePage from './components/CreatePage'
import EditPage from './components/EditPage'
import Delete from './components/Delete'
import Navbar from './components/navbar/Navbar'

function App() {

  return (
    <>
      <Navbar content={
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/create" element={<CreatePage />} />
          <Route path="/edit/:id" element={<EditPage />} />
          <Route path="/delete/:id" element={<Delete />} />
        </Routes>}/>
    </>
  )
}

export default App
