import styles from "./Form.module.css"
import { Button } from "../Button/Button"


export function Form(props) {
    /* Форма для ввода данных с дочерними элементами*/
    const {children} = props
    console.log(children[0])

    return (
        <div className={styles.Form}>
            <div className={styles.data}>
                <p>{`data = {`}</p>
                {
                    children.map(
                        (children) => {
                            return <p className={styles.WithMargin}>&emsp;&emsp;&emsp;{children.props.fieldName}: {children},</p>
                        }
                    )
                }
                <p>{`}`}</p>
            </div>
            <Button id={styles.formButton} text="Send"/>
        </div>
    )
}
