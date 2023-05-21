import styles from "./Form.module.css"
import { Button } from "../Button/Button"


export function Form(props) {
    /* Форма для ввода данных с дочерними элементами*/
    const {children, buttonText, onClickButton} = props

    return (
        <div className={styles.Form}>
            <div className={styles.data}>
                <p>{`data = {`}</p>
                {
                    children.map(
                        (ch, index) => <p key={index} className={styles.WithMargin}>&emsp;&emsp;&emsp;{ch.props.fieldname}: {ch},</p>
                    )
                }
                <p>{`}`}</p>
            </div>
            <Button id={styles.formButton} text={buttonText} onClickButton={onClickButton}/>
        </div>
    )
}
