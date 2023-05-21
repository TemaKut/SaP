import styles from "./Form.module.css"
import { Button } from "../Button/Button"
import { ErrorFormMessage } from "../ErrorFormMessage/ErrorFormMessage"


export function Form(props) {
    /* Форма для ввода данных с дочерними элементами*/
    const {children, buttonText, onClickButton, formError} = props

    return (
        <div className={styles.Form}>
            <div className={styles.data}>
                <p>{`data = {`}</p>
                {
                    children.map(
                        (ch, index) => <p key={index} className={styles.WithMargin}>&emsp;&emsp;{ch.props.fieldname}: {ch},</p>
                    )
                }
                <p>{`}`}</p>
            </div>
            {
                formError
                ?<ErrorFormMessage response={formError}/>
                : null
            }
            <Button id={styles.formButton} text={buttonText} onClickButton={onClickButton}/>
        </div>
    )
}
