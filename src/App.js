import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [link_from_bic,setlink_from_bic] = useState(null);
    const [time_min,settime_min] = useState(null);
    const [bank_bic,setbank_bic] = useState(null);
    const [bank_charge,setbank_charge] = useState(null);
    const [user_name,setuser_name] = useState(null);
    const [user_bal,setuser_bal] = useState(null);
    const [user_ac,setuser_ac] = useState(null);
    const [Admin_select, setAdmin_select] = useState(null);
    const [role, setRole] = useState(null);
    const [name, setname] = useState(null);
    const [from_acc, setfrom_acc] = useState(null);
    const [to_acc, setto_acc] = useState(null);
    const [from_bic, setfrom_bic] = useState(null);
    const [to_bic, setto_bic] = useState(null);
    const [amount, setamount] = useState('');
    const [user_bic,setuser_bic] = useState(null);

    const find_fast_route = () => {
        axios.post('http://localhost:5000/enter_raffle', { name:name,from_acc: from_acc,to_acc:to_acc,from_bic:from_bic, to_bic:to_bic,amount:amount})
            .then(response => alert(response.data.message))
            .catch(error => console.error('Error:', error));
    };

    const find_cheap_route = () => {
        axios.post('http://localhost:5000/accept_spot', { name:name,from_acc: from_acc,to_acc:to_acc,from_bic:from_bic, to_bic:to_bic,amount:amount })
            .then(response => alert(response.data.message))
            .catch(error => console.error('Error:', error));
    };

    const add_user = () => {
        // axios.post('http://localhost:5000/decline_spot', { ac_no: ac_no,user_bic:user_bic,user_bal:user_bal })
        //     .then(response => alert(response.data.message))
        //     .catch(error => console.error('Error:', error));
    };

    const add_bank = () => {
        // axios.post('http://localhost:5000/set_spot_availability', { bank_bic: bank_bic,bank_charge:bank_charge })
        //     .then(response => alert(response.data.message))
        //     .catch(error => console.error('Error:', error));
    };

    const add_link = () => {
        // axios.post('http://localhost:5000/assign_slot', { link_from_bic: link_from_bic,to_bic:to_bic,time_min:time_min })
        //     .then(response => alert(response.data.message))
        //     .catch(error => console.error('Error:', error));
    };

    return (
        <div className="app-container">
            <h1>Fund Tranfer System</h1>
            <div className="role-buttons">
                <button onClick={() => setRole('User')}>User</button>
                {/* <button onClick={() => setRole('Slot Owner')}>Slot Owner</button> */}
                <button onClick={() => setRole('Admin')}>Admin</button>
            </div>
            {role === 'User' && (
                <div className="role-section">
                    <h2> Transaction </h2>
                    <input type='text' placeholder='Enter Name' value={name} onChange={e => setname(e.target.value)} />
                    <input type='text' placeholder='Enter A/C Number' value={from_acc} onChange={e => setfrom_acc(e.target.value)} />
                    <input type='text' placeholder='Enter Target A/C Number' value={to_acc} onChange={e => setto_acc(e.target.value)} />
                    <input type='text' placeholder='From ' value={from_bic} onChange={e => setfrom_bic(e.target.value)} />
                    <input type='text' placeholder='To' value={to_bic} onChange={e => setto_bic(e.target.value)} />
                    <input type='text' placeholder='Amount ' value={amount} onChange={e => setamount(e.target.value)} />

                    <button onClick={find_fast_route}>Find Fast Route</button>
                    <button onClick={find_cheap_route}>Find Cheap Cost</button>
                </div>
            )}
            
        </div>
    );
}

export default App;
